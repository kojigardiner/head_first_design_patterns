class Amplifier:
    def __init__(self):
        pass


class Tuner:
    def __init__(self):
        pass


class StreamingPlayer:
    def __init__(self):
        pass


class Projector:
    def __init__(self):
        pass


class TheaterLights:
    def __init__(self):
        pass


class Screen:
    def __init__(self):
        pass


class PopcornPopper:
    def __init__(self):
        pass


class HomeTheaterFacade:
    amp: Amplifier
    tuner: Tuner
    player: StreamingPlayer
    projector: Projector
    lights: TheaterLights
    screen: Screen
    popper: PopcornPopper

    def __init__(
        self,
        amp: Amplifier,
        tuner: Tuner,
        player: StreamingPlayer,
        projector: Projector,
        lights: TheaterLights,
        screen: Screen,
        popper: PopcornPopper,
    ):
        self.amp = amp
        self.tuner = tuner
        self.player = player
        self.projector = projector
        self.lights = lights
        self.screen = screen
        self.popper = popper

    # note, not all methods below have been defined
    def watch_movie(self, movie: str):
        print("Get ready to watch a movie..."):
        popper.on()
        popper.pop()
        lights.dim(10)
        screen.down()
        projector.on()
        projector.widescreen_mode()
        amp.on()
        amp.set_streaming_player(player)
        amp.set_surround_sound()
        amp.set_volume(5)
        player.on()
        player.play(movie)


    def end_movie(self):
        popper.off()
        lights.on()
        screen.up()
        projector.off()
        amp.off()
        player.stop()
        player.off()
