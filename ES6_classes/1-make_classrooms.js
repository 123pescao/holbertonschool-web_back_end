import ClassRoom from "./0-classroom";

/**
 * Initializes an array of ClassRoom objects with specific capacities.
 * @returns {ClassRoom[]} Array of ClassRoom objects.
 */
const initializeRooms = () => {
    const ROOM_CAPACITY_LARGE = 34,
        ROOM_CAPACITY_MEDIUM = 20,
        ROOM_CAPACITY_SMALL = 19,

        rooms = [
            new ClassRoom(ROOM_CAPACITY_SMALL),
            new ClassRoom(ROOM_CAPACITY_MEDIUM),
            new ClassRoom(ROOM_CAPACITY_LARGE)
        ];

    return rooms;
};

export default initializeRooms;