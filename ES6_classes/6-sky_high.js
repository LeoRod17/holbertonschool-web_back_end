import Building from './5-building';

export default class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    super(sqft);
    this._floors = floors;
  }

  get sqft() {
    return this._sqft;
  }

  get floors() {
    return this._floors;
  }

  set floors(newFloor) {
    if (typeof (newFloor) === 'number') {
      this._floors = newFloor;
    } else {
      throw TypeError('TypeError: floors must be a number');
    }
  }

  evacuationWarningMessage() {
    return `Evacuate slowly the ${this._floors} floors.`;
  }
}
