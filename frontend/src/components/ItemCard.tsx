import "../styles/PetCard.css";

interface DataProps {
    category: string;
    stock: number;
    cost: number;
    description: string;
    name: string;
    img_src: string;
    id: number;
}

function ItemCard({
  stock,
  cost,
  description,
  name,
  category,
  id
}: DataProps) {
    const img_src = 
    category === "Toys" ? `../public/toy${id}.png` :
    category === "Food" ? `../public/food${id}.png` :
    category === "Beds" ? `../public/bed${id}.png` :
    category === "Accessories" ? `../public/accessory${id}.png` : "";
    
  return (
    <>
      <div className="card">
        <img src={img_src} alt={`${category} image`}></img>
        <p style={{fontWeight: "bold"}}>{(name)}</p>
        <p>{(description)}</p>
        <p>Cost: ${(cost)}</p>
        <p>Stock: {(stock)}</p>
      </div>
    </>
  );
}

export default ItemCard;
