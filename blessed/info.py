import blessed

def labeled_text(t, label, text):
    width = len(label) + len(text) + 3

    print(t.bold_on_green(' '*width))
    print(t.bold_on_green(' '), end='')
    print(t.bold_on_blue('{}:{}'.format(label, text)), end='')
    print(t.bold_on_green(' '))
    print(t.bold_on_green(' '*width))

class BlessedApp(object):
    def __init__(self, title=None):
        self.title = title

    def init(self):
        self.t = blessed.Terminal()

    def _render_title_bar(self):
        msg = ' Title: {}'.format(self.title)
        print(self.t.bold_white_on_blue(msg), end='')
        print(self.t.bold_on_blue(' '*(self.t.width - len(msg))))

    def _render_status_bar(self):
        msg = ' Status: {} x {}'.format(
            self.t.width,
            self.t.height
        )

        print(self.t.bold_white_on_blue('{}'.format(msg)), end='')
        print(self.t.bold_on_blue(' '*(self.t.width - len(msg))))

    def render(self):
        with self.t.hidden_cursor(), \
             self.t.fullscreen():
            for row in iter(range(self.t.height - 1)):
                if row == 0:
                    self._render_title_bar()

                elif row == self.t.height - 1:
                    self._render_status_bar()

                elif row < self.t.height - 1:
                    for col in iter(range(self.t.width)):
                        if col == 0:
                            print(self.t.bold_on_blue(' '), end='')
                        elif col == self.t.width - 1:
                            print(self.t.bold_on_blue(' '))
                        else:
                            print(self.t.bold_on_black(' '), end='')

    def run(self):
        self.render()
        inp = None
        while True:
            inp = self.t.inkey()

            if inp == chr(3):
                # ^c exits
                break


def main():
    t = blessed.Terminal()
    t.clear()
    # print(t.bold_red('Terminal Info:'))
    # print(t.bold('\theight:{}'.format(t.height)))
    # print(t.bold('\twidth:{}'.format(t.width)))

    # labeled_text(t, 'test', 'value')
    a = BlessedApp(title='Test App')
    a.init()
    a.run()

    #with t.location(0, t.height - 1):
    #    print(t.center(t.blink('press any key to continue.')))

    with t.cbreak():
        inp = t.inkey()
        print('input: {}'.format(inp))


if __name__ == '__main__':
    main()
