import { useNavigate } from 'react-router-dom';
import '../styles/ShopButton.css';
interface typeProps {
    type: string;
}

function ShopButton({ type }: typeProps){
    const navigate = useNavigate();

    const handleClick = () => {
        navigate(`/shop/${type}`);
    };

    return(
        <>
            <div className="shop_container">
                <button className="btn" id={`${type}`} onClick={handleClick}><img className="shop_logo" src={`${type}.png`} alt={type}/></button>
                <p>{type}</p>
            </div>
        </>
    )
}

export default ShopButton;