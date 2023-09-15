export default class Building {
  constructor(sqft) {
    if (this.constructor !== Building && this.evacuationWarningMessage === undefined) {
      throw new Error('Class extending Building must override evacuationWarningMessage');
    }
    if (typeof (sqft) === 'number') {
      this._sqft = sqft;
    } else {
      throw TypeError('TypeError: sqft must be a number');
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
}
