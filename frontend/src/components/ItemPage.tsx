import { useEffect, useState } from "react";
import ItemCard from "./ItemCard";

interface ItemPageProps{
    filterCategory: string;
}

function ItemPage({filterCategory} : ItemPageProps) {
  // State to store dog data from the API
  const [items, setItems] = useState<any[]>([]); // eslint-disable-line @typescript-eslint/no-explicit-any

    // Fetch data from the API on component mount
    useEffect(() => {
        const fetchItems = async () => {
            try {
                const response = await fetch("http://127.0.0.1:5001/items_get");
                if (!response.ok) {
                    throw new Error("Failed to fetch Items");
                }
                const data = await response.json();
                console.log("Fetched data:", data); // Add this line
                const flattenedItems = Object.values(data).flat(); // Flatten grouped items into one array
                const filteredItems = filterCategory  // eslint-disable-line @typescript-eslint/no-explicit-any
                ? flattenedItems.filter((item: any) => item.category === filterCategory)  // eslint-disable-line @typescript-eslint/no-explicit-any
                : flattenedItems;
                setItems(filteredItems);
                
            } catch (error) {
                console.error("Error fetching items:", error);
            }
        };
    
        fetchItems();
    }, []);

    const splitItems = (array: any[], rowSize: number) => {  // eslint-disable-line @typescript-eslint/no-explicit-any
        const splitArray = []; 
        for (let i = 0; i < array.length; i += rowSize) {
            splitArray.push(array.slice(i, i + rowSize));
        }
        return splitArray;
    }

    const rows = splitItems(items, 4);

    return (
        <div className="row">
            <table style={{ marginLeft: "23px", borderCollapse: "collapse" }}>
                <tbody>
                    {rows.map((items, rowIndex) => (
                        <tr key={rowIndex}>
                            {items.map((item) => (
                                <td key={item.id}>
                                    <ItemCard
                                        stock = {item.stock}
                                        cost = {item.cost}
                                        description = {item.description}
                                        name= {item.name}
                                        img_src = {item.img_src}
                                        id={item.id}
                                        category={item.category}
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

export default ItemPage;
