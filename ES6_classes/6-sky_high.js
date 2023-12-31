import Building from './5-building';

export default class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    super(sqft);
    if (typeof (floors) === 'number') {
      this._floors = floors;
    } else {
      throw TypeError('TypeError: floors must be a number');
    }
  }

  get sqft() {
    return this._sqft;
  }

  set sqft(newSqft) {
    if (typeof (newSqft) === 'number') {
      this._sqft = newSqft;
    } else {
      throw TypeError('TypeError: sqft must be a number');
    }
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
    return `Evacuate slowly the ${this._floors} floors`;
  }
}
