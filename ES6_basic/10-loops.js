export default function appendToEachArrayValue(array, appendString) {
  const lista = [];
  for (const idx of array) {
    lista.push(appendString + idx);
  }

  return lista;
}
