import badge, asyncio

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

        self.received_message = None

    def on_open(self):
        badge.display.fill(1)
        image = badge.display.import_pbm("apps/william/sprites.pbm")
        badge.display.blit(image, 0, 0)
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

        if self.received_message:
            badge.display.fill(1)
            badge.display.text(f"Received: {self.received_message}", 0, 0, 0)
            badge.display.show()
            print(f"Received packet: {self.received_message}")
            asyncio.create_task(self.notify())
            self.received_message = None

    def on_packet(self, packet: badge.radio.Packet, in_foreground: bool):
        self.received_message = packet.data

    async def siren(self) -> None:
        """
        Siren the LED to indicate a new message.
        This async function runs on the OS thread - make sure it yields properly.
        """
        for i in range(0, 65535, 5000):
            badge.utils.set_led_pwm(i)
            await asyncio.sleep(0.05)
        badge.utils.set_led(True)
        for i in range(65535, 0, -5000):
            badge.utils.set_led_pwm(i)
            await asyncio.sleep(0.05)
        badge.utils.set_led_pwm(0)

    async def ring(self) -> None:
        """
        Ring the buzzer to indicate a new message.
        This async function runs on the OS thread - make sure it yields properly.
        """
        # siren the buzzer - for loop with audible tones
        badge.buzzer.tone(523, 0.5)  # C5
        await asyncio.sleep(0.1)
        badge.buzzer.tone(392, 0.25)  # G4
        await asyncio.sleep(0.05)
        badge.buzzer.tone(392, 0.25)  # G4
        await asyncio.sleep(0.05)
        badge.buzzer.tone(415, 0.5)  # G#4
        await asyncio.sleep(0.1)
        badge.buzzer.tone(392, 0.5)  # G4
        await asyncio.sleep(0.6)
        badge.buzzer.tone(493, 0.5)  # B4
        await asyncio.sleep(0.1)
        badge.buzzer.tone(523, 0.5)  # C5
        await asyncio.sleep(0.1)
        badge.buzzer.no_tone()
        
    async def notify(self) -> None:
        """
        Asynchronously notify the user of a new message.
        """

        # is this the right way to do this?
        await self.siren()
        await self.ring()
        await self.siren()