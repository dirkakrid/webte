import tornado.websocket
import pyte


class TerminalWebSocket(tornado.websocket.WebSocketHandler):

    def open(self):
        self.stream = pyte.ByteStream()
        self.screen = pyte.Screen(80, 24)
        self.stream.attach(self.screen)
        self.proc = tornado.process.Subprocess(
            "ssh -tt localhost", shell=True,
            stdin=tornado.process.Subprocess.STREAM,
            stdout=tornado.process.Subprocess.STREAM,
            stderr=tornado.process.Subprocess.STREAM)
        self.stdout = self.proc.stdout
        self.stderr = self.proc.stderr
        self.stdin = self.proc.stdin
        self.stdout.read_until_close(
            callback=self.on_close, streaming_callback=self.on_process_read)
        self.stderr.read_until_close(
            callback=self.on_close, streaming_callback=self.on_process_read)

    def on_message(self, message):
        self.stdin.write_to_fd(bytes([int(message.encode())]))

    def on_process_read(self, text):
        self.stream.feed(text)
        self.write_message("\n".join(self.screen.display))

    def on_close(self):
        self.proc.proc.terminate()
