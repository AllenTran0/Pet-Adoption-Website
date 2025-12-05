import "../styles/PetCard.css";
import { check } from "../components/Check";

interface DataProps {
  breed: string;
  specific_breed: boolean;
  service_type: boolean;
  hyper_allergenic: boolean;
  house_trained: boolean;
  img_src: string;
  animal_type: "dog" | "cat";
  id: number;
}

function PetCard({
  breed,
  specific_breed,
  service_type,
  hyper_allergenic,
  house_trained,
  animal_type,
  id
}: DataProps) {
  //Breed should be name of the animal or actual breed temporary for now
  //Temp image for now

    const img_src = animal_type === "dog" ? `dog${id}.png` : `cat${id}.png`;

  return (
    <>
      <div className="card">
        <h2>{breed}</h2>
        <img src={img_src} alt={`${animal_type} image`}></img>
        <p>Specific Breed: {check(specific_breed)}</p>
        <p>Service Type: {service_type ? "Yes" : "No"}</p>
        <p>Hyper Allergenic: {hyper_allergenic ? "Yes" : "No"}</p>
        <p>House Trained: {house_trained ? "Yes" : "No"}</p>
      </div>
    </>
  );
}

export default PetCard;
