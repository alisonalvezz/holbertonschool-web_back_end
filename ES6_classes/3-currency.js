export default class Currency {
  constructor(name, code) {
    this._code = code;
    this._name = name;
  }
  get code() {
    return this._code;
  }

  set code(value) {
    this._code = value
  }

  get name() {
    return this._name;
  }
  
  set name(value) {
    if (typeof value !== 'string') {
        throw new TypeError('Name must be a string');
    }
    this._name = value;
  }

  displayFullCurrency() {
    return `${this.code} (${this.name})`
  }
}
