import { uploadPhoto, createUser } from "./utils";
export default function handleProfileSignup() {
  Promise.all([uploadPhoto, createUser]).then((values) => {
    console.log(values);
  });
}
