from abc import ABC, abstractmethod

class ElevatorError(Exception):
    pass

# raise ElevatorError("This is an error")

@abstractmethod
class ButtonInterface(ABC):
    @abstractmethod
    def press(self):
        pass

    @abstractmethod
    def reset(self):
        pass

class InsideButton(ButtonInterface):
    def __init__(self, floor_num) -> None:
        self.floor_num = floor_num
        self.is_pressed = False

    def press(self):
        self.is_pressed = True

    def reset(self):
        self.is_pressed = False

class OutsideButton(ButtonInterface):
    def __init__(self, floor_number, direction):
        self.floor_number = floor_number
        self.direction = direction  # "up" or "down"
        self.is_pressed = False

    def press(self):
        self.is_pressed = True

    def reset(self):
        self.is_pressed = False

# class Button:
#     def __init__(self, floor_num) -> None:
#         self.floor_num = floor_num
#         self.is_pressed = False
        
#     def press(self):
#         self.is_pressed = True

#     def reset(self):
#         self.is_pressed = False


class Elevator:
    def __init__(self, elevator_id, total_floors) -> None:
        self.elevator_id = elevator_id
        self.current_floor = 0
        self.direction = "idle"
        self.status = "stopped"
        self.buttons = [InsideButton(i) for i in range(total_floors)]
        #self.requested_floors = set()

    @property
    def requested_floors(self):
        return [button.floor_number for button in self.buttons if button.is_pressed]
    
    def request_floor(self, floor):
        self.buttons[floor].press()
        while self.current_floor != floor:
            self.update_direction_and_status()
            self.move()

    def update_direction_and_status(self):
        # direction, status 
        # up, down, idle / stopped, moving
        if self.current_floor in self.request_floor:
            self.status = "stopped"
            # self.request_floor.remove(self.current_floor)
            self.buttons[self.current_floor].reset()

        elif any(floor > self.current_floor for floor in self.requested_floors):
            self.direction = "up"
            self.status = "moving"

        elif any(floor < self.current_floor for floor in self.requested_floors):
            self.direction = "down"
            self.status = "moving"

        else:
            self.direction = "idle"
            self.status = "stopped"

        
    def move(self):
        # action up
        # action down
        if self.direction == "up":
            self.current_floor += 1

        elif self.direction == "down":
            self.current_floor -= 1
        self.update_direction_and_status()


    def __str__(self) -> str:
        print("sth")
        
class ElevatorController:
    def __init__(self, total_elevators, total_floors) -> None:
        self.elevators = [Elevator(i, total_floors) for i in range(total_elevators)]

        
    def request_elevator(self, floor, direction):
        # request algo
        chosen_elevator = None
        for elevator in self.elevators:
            if elevator.status == "stopped" and elevator.direction == "idle":
                chosen_elevator = elevator
                break
            
        # if first elevator moving in the requested direction
        if not chosen_elevator:
            for elevator in self.elevators:
                if elevator.direction == direction:
                    chosen_elevator = elevator
                    break
        if not chosen_elevator:
            chosen_elevator = self.elevators[0]          
            
        if floor > chosen_elevator.current_floor:
            chosen_elevator.direction = "up"
        elif floor < chosen_elevator.current_floor:
            chosen_elevator.direction = "down"

        # Move the elevator to the requested floor using the existing move() method
        while chosen_elevator.current_floor != floor:
            chosen_elevator.move()

        chosen_elevator.direction = "idle"
        chosen_elevator.status = "stopped"
        return chosen_elevator
    

    def get_elevator_status(self):
        return [str(elevator) for elevator in self.elevators]

class Building:
    def __init__(self, total_elevators, total_floors) -> None:
        self.total_floors = total_floors
        self.elevator_controller = ElevatorController(total_elevators, total_floors)
         # Create outside buttons
        self.outside_buttons = {}
        for floor in range(total_floors):
            if floor == 0:
                self.outside_buttons[(floor, "up")] = OutsideButton(floor, "up")
            elif floor == total_floors - 1:
                self.outside_buttons[(floor, "down")] = OutsideButton(floor, "down")
            else:
                self.outside_buttons[(floor, "up")] = OutsideButton(floor, "up")
                self.outside_buttons[(floor, "down")] = OutsideButton(floor, "down")
   
    def request_elevator(self, floor, direction):
        # Check if the button press is valid
        if (floor, direction) not in self.outside_buttons:
            raise ElevatorError(f"No {direction} button for floor {floor}.")
        
        self.outside_buttons[(floor, direction)].press()
        return self.elevator_controller.request_elevator(floor, direction)

    
    def get_elevator_status(self):
        return self.elevator_controller.get_elevator_status()
    

building = Building(8, 100)
elevator = building.request_elevator(4, "up")

elevator.request_floor(10)
elevator.move()
building.status 
