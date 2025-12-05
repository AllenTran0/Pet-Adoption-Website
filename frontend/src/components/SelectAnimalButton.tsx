import { useNavigate } from 'react-router-dom';

interface AnimalImageProps {
    animal: string; // Define animal as a string type
}

function PetButton ({ animal }: AnimalImageProps){
    const navigate = useNavigate();

    const handleClick = () => {
        navigate(`/${animal}`);
    };

    return(
        <>
            <div className="animal_container">
                <button className="btn" id={`${animal}`} onClick={handleClick}><img src={`${animal}.png`} alt={animal}/></button>
            </div>
        </>
    )
}

export default PetButton;