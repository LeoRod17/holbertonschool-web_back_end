export default function concatArrays(array1, array2, string) {
  const ar = [...array1, ...array2, ...string];
  return ar
}