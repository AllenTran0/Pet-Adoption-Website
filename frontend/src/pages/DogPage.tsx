import { useEffect, useState } from "react";
import PetCard from "../components/PetCard";

function DogPage() {
  // State to store dog data from the API
  const [dogs, setDogs] = useState<any[]>([]); // eslint-disable-line @typescript-eslint/no-explicit-any

    // Fetch data from the API on component mount
    useEffect(() => {
        const fetchDogs = async () => {
            try {
                const response = await fetch("http://127.0.0.1:5001/pets_get"); // Update with your actual API endpoint
                if (!response.ok) {
                    throw new Error("Failed to fetch dogs");
                }
                const data = await response.json();
                setDogs(data.dogs);
            } catch (error) {
                console.error("Error fetching dogs:", error);
            }
        };

    fetchDogs();
  }, []);

    const splitDogs = (array: any[], rowSize: number) => {  // eslint-disable-line @typescript-eslint/no-explicit-any
        const splitArray = []; 
        for (let i = 0; i < array.length; i += rowSize) {
            splitArray.push(array.slice(i, i + rowSize));
        }
        return splitArray;
    }

    const rows = splitDogs(dogs, 4);

    return (
        <div className="row">
            <table style={{ marginLeft: "23px" }}>
                <tbody>
                    {rows.map((dogs, rowIndex) => (
                        <tr key={rowIndex}>
                            {dogs.map((dog) => (
                                <td key={dog.id}>
                                    <PetCard
                                        breed={dog.breed}
                                        specific_breed={dog.specific_breed === "True"}
                                        service_type={dog.service_type === "True"}
                                        hyper_allergenic={dog.hyper_allergenic === "True"}
                                        house_trained={dog.house_trained === "True"}
                                        img_src={dog.img_src}
                                        animal_type={dog.animal_type === "cat" ? "cat" : "dog"}
                                        id={dog.id}
                                    />
                                </td>
                            ))}
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default DogPage;
