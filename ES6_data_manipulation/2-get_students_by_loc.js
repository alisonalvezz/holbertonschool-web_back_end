export default function getStudentsByLocation(arrayObject, city) {
  return arrayObject.filter((obj) => obj.location === city);
}
