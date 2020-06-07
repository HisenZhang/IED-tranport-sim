from simulator.core import Simulator


def main():
    # Setup simulator with step = 1 min
    sim = Simulator(step=60000)

    # Main loop
    while sim.isRunning():
        sim.update()


if __name__ == '__main__':
    main()
