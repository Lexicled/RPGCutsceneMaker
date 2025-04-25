import time
from command import Command

class Timeline:
    _instance = None

    def __init__(self):
        raise RuntimeError('Call instance() instead')

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls) # Singleton pattern implementation

            cls.total_length = 0
            cls.commands: list[Command] = []
            cls.current_timestamp = 0

        return cls._instance
    
    def add_command(self, command: Command):
        self.commands.append(command)
    
    def move_to_time(self, timestamp: int):
        # TODO add requirements functionality
        self.current_timestamp = timestamp
        for cmd in self.commands:
            if cmd.start <= self.current_timestamp and cmd.end >= self.current_timestamp:
                cmd.action() # Run command's action if necessary
    
    def move_forward(self, ticks_per_second: int):
        while self.current_timestamp < self.total_length:
            ms_per_tick = int((ticks_per_second ** (-1)) * 1000)

            start = int(time.time() * 1000)
            self.move_to_time(self.current_timestamp + 1)
            end = int(time.time() * 1000)

            while end - start < ms_per_tick:
                end = int(time.time() * 1000) # Ensure timing is not too fast
    
    def sort_commands(self):
        # Bubble sort - feel free to replace with something more efficient if you have free time
        sort = False
        while not sort:
            sort = True
            last = None
            i = 0
            for cmd in self.commands:
                if last == None or i == 0:
                    last = cmd.start
                    i += 1
                    continue
                if cmd.start <= last:
                    self.commands[i], self.commands[i - 1] = self.commands[i - 1], self.commands[i]
                    sort = False
                last = cmd.start
                i += 1
    
    def export(self, sleep_function: str, ticks_per_second: int): # Sleep function: same format as Command.syntax, but with one int parameter of rest time in ms
        # TODO add requirements functionality
        self.sort_commands()
        ms_per_tick = int((ticks_per_second ** (-1)) * 1000)
        export_data = ""
        
        if len(self.commands) > 0 and self.commands[0].start != 0:
            time_delay_ticks = self.commands[0].start
            time_delay_ms = ms_per_tick * time_delay_ticks
            sleep_elements = sleep_function.split('|')
            sleep_string = sleep_elements[0] + str(time_delay_ms) + sleep_elements[2]
            export_data += sleep_string

        n = 0
        for cmd in self.commands:
            elements = cmd.syntax.split('|')
            new_elements = []

            i = 0
            for element in elements:
                if i != 0 and i % 2 != 0:
                    new_elements.append(cmd.params[element])
                    i += 1
                else:
                    new_elements.append(element)
                    i += 1

            for new_element in new_elements:
                export_data += new_element

            export_data += "\n"
            if n < len(self.commands):
                time_delay_ticks = self.commands[n + 1].start - cmd.start
                time_delay_ms = ms_per_tick * time_delay_ticks
                sleep_elements = sleep_function.split('|')
                sleep_string = sleep_elements[0] + str(time_delay_ms) + sleep_elements[2]
                export_data += sleep_string
            n += 1



def test_timeline_and_command():
    class TestCmd(Command):
        def __init__(self, syntax, start, end, parameters = ..., specific_params = ..., requirements = ..., tag = "", visible = True):
            self.test_action_run_count = 0
            super().__init__(syntax, start, end, parameters, specific_params, requirements, tag, visible)

        def action(self):
            self.test_action_run_count += 1


    test_cmd = TestCmd(10, 20)
    test_timeline = Timeline.instance()
    test_timeline.add_command(test_cmd)
    test_timeline.total_length = 40

    start = int(time.time() * 1000)
    test_timeline.move_forward(20)
    end = int(time.time() * 1000)

    print("Ran with no syntax errors...")
    assert test_cmd.test_action_run_count == 11, f"Ran action() {test_cmd.test_action_run_count} times where should have run 11 times"
    print("action() ran correct number of times...")
    assert end - start == 2000, f"Took {end - start}ms to run where should have taken 2000ms"
    print("Timing is correct...")
    # TODO add test for export function
    print("Tests finished successfully with no errors!")

