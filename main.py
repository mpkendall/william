import badge

class App(badge.BaseApp):
    def __init__(self):
        self.old_button_a = False
        self.old_button_b = False
        self.old_button_c = False
        self.old_button_d = False
        self.old_button_e = False
        self.old_button_f = False
        self.old_button_g = False
        self.old_button_h = False
        self.old_button_i = False
        self.old_button_j = False
        self.old_button_k = False
        self.old_button_l = False

    def on_open(self):
        badge.display.fill(1) 
        badge.display.text("William Daniel", 0, 0, 0)
        badge.display.show()

    def loop(self):
        if badge.input.get_button(badge.input.Buttons.SW17):
            self.old_button_a = True
        else:
            if self.old_button_a:
                print("Button A pressed")
                badge.radio.send_packet(0x5128, b'have:cable')
            self.old_button_a = False

        if badge.input.get_button(badge.input.Buttons.SW10):
            self.old_button_b = True
        else:
            if self.old_button_b:
                print("Button B pressed")
                badge.radio.send_packet(0x5128, b'have:writing')
            self.old_button_b = False

        if badge.input.get_button(badge.input.Buttons.SW18):
            self.old_button_c = True
        else:
            if self.old_button_c:
                print("Button C pressed")
                badge.radio.send_packet(0x5128, b'have:food')
            self.old_button_c = False

        if badge.input.get_button(badge.input.Buttons.SW9):
            self.old_button_d = True
        else:
            if self.old_button_d:
                print("Button D pressed")
                badge.radio.send_packet(0x5128, b'have:charge')
            self.old_button_d = False

        if badge.input.get_button(badge.input.Buttons.SW15):
            self.old_button_e = True
        else:
            if self.old_button_e:
                print("Button E pressed")
                badge.radio.send_packet(0x5128, b'come:sos')
            self.old_button_e = False

        if badge.input.get_button(badge.input.Buttons.SW8):
            self.old_button_f = True
        else:
            if self.old_button_f:
                print("Button F pressed")
                badge.radio.send_packet(0x5128, b'come:assist')
            self.old_button_f = False

        if badge.input.get_button(badge.input.Buttons.SW16):
            self.old_button_g = True
        else:
            if self.old_button_g:
                print("Button G pressed")
                badge.radio.send_packet(0x5128, b'come:bored')
            self.old_button_g = False

        if badge.input.get_button(badge.input.Buttons.SW7):
            self.old_button_h = True
        else:
            if self.old_button_h:
                print("Button H pressed")
                badge.radio.send_packet(0x5128, b'location:shelbrooke')
            self.old_button_h = False

        if badge.input.get_button(badge.input.Buttons.SW13):
            self.old_button_i = True
        else:
            if self.old_button_i:
                print("Button I pressed")
                badge.radio.send_packet(0x5128, b'location:main')
            self.old_button_i = False

        if badge.input.get_button(badge.input.Buttons.SW6):
            self.old_button_j = True
        else:
            if self.old_button_j:
                print("Button J pressed")
                badge.radio.send_packet(0x5128, b'location:dining')
            self.old_button_j = False

        if badge.input.get_button(badge.input.Buttons.SW14):
            self.old_button_k = True
        else:
            if self.old_button_k:
                print("Button K pressed")
                badge.radio.send_packet(0x5128, b'location:dock')
            self.old_button_k = False

        if badge.input.get_button(badge.input.Buttons.SW5):
            self.old_button_l = True
        else:
            if self.old_button_l:
                print("Button L pressed")
                badge.radio.send_packet(0x5128, b'location:waterfront')
            self.old_button_l = False

    def on_packet(self, packet: badge.radio.Packet, in_foreground: bool):
        badge.display.fill(1)
        badge.display.text(f"{packet.data}", 0, 0, 0)
        badge.display.show()
        print(f"Received packet: {packet}")