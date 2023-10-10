export default function createInt8TypedArray(length, position, value) {
  const lista = new Int8Array(length);
  if (position > length) {
    throw Error('Position outside range');
  }
  lista[position] = value;
  const { buffer } = lista;
  return new DataView(buffer, 0, length);
}
