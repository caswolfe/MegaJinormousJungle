from src import NetworkActionHandler, DataPacket


class SocketHandler:

    def __init__(self):
        pass

    def establish_connection(self) -> None:
        pass

    def close_connection(self) -> None:
        pass

    def open_as_host(self) -> bool:
        pass

    def close_as_host(self) -> None:
        pass

    def add_network_action_handler(self, nah: NetworkActionHandler) -> None:
        pass

    def remove_network_action_handler(self, nah: NetworkActionHandler) -> bool:
        pass

    def send_packet(self, dp: DataPacket) -> bool:
        pass
