class Flight:
    def __init__(self, engine):
        self.engine = engine

    def startEngine(self):
        self.engine.start()


class AirbusEngine:
    def start(self):
        print("Airbus Engine is starting and ready to take a flight")


class BoingEngine:
    def start(self):
        print("This is boeing engine that is ready to start and take a flight")


ae = AirbusEngine()
f = Flight(ae)
f.startEngine()

be = BoingEngine()
f1 = Flight(be)
f1.startEngine()