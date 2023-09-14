export default function returnHowManyArguments(...Array) {
  let i = 0;
  while (i in Array) {
    i += 1;
  }
  return i;
}
