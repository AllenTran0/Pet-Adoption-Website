import { useEffect, useState } from "react";
import PetCard from "../components/PetCard";

function CatPage() {
  // State to store dog data from the API
  const [cats, setCats] = useState<any[]>([]); // eslint-disable-line @typescript-eslint/no-explicit-any

    // Fetch data from the API on component mount
    useEffect(() => {
        const fetchCats = async () => {
            try {
                const response = await fetch("http://127.0.0.1:5001/pets_get"); // Update with your actual API endpoint
                if (!response.ok) {
                    throw new Error("Failed to fetch cats");
                }
                const data = await response.json();
                setCats(data.cats);
            } catch (error) {
                console.error("Error fetching cats:", error);
            }
        };

    fetchCats();
  }, []);

    const splitCats = (array: any[], rowSize: number) => {  // eslint-disable-line @typescript-eslint/no-explicit-any
        const splitArray = []; 
        for (let i = 0; i < array.length; i += rowSize) {
            splitArray.push(array.slice(i, i + rowSize));
        }
        return splitArray;
    }

    const rows = splitCats(cats, 4);

    return (
        <div className="row">
            <table style={{ marginLeft: "23px" }}>
                <tbody>
                    {rows.map((cats, rowIndex) => (
                        <tr key={rowIndex}>
                            {cats.map((cat) => (
                                <td key={cat.id}>
                                    <PetCard
                                        breed={cat.breed}
                                        specific_breed={cat.specific_breed === "True"}
                                        service_type={cat.service_type === "True"}
                                        hyper_allergenic={cat.hyper_allergenic === "True"}
                                        house_trained={cat.house_trained === "True"}
                                        img_src={cat.img_src}
                                        animal_type={cat.animal_type === "dog" ? "dog" : "cat"}
                                        id={cat.id}
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

export default CatPage;
