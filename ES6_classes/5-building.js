// Default square footage value
const DEFAULT_SQFT = 0;

export default class Building {
    constructor(sqft = DEFAULT_SQFT) {
        if (
            this.constructor !== Building &&
            typeof this.evacuationWarningMessage !== "function"
        ) {
            throw new Error("Class extending Building must override " +
                "evacuationWarningMessage");
        }

        this._sqft = sqft;
    }

    // Static getter for default square footage
    static get defaultSqft() {
        return DEFAULT_SQFT;
    }

    // Getter for square footage
    get sqft() {
        return this._sqft;
    }
}