import "../styles/Home.css";
import PetButton from "../components/SelectAnimalButton";

//Home webpage for pet adoption website
function Home(){
    return (
        <>
            <div className="app">
                <div className="main-content">

                    <div>
                        <img className="cat_logo" src="home_cat.png"/>
                    </div>

                    <div className="text_container">
                        <p className="select_text">Choose an Animal!</p>
                    </div>

                    <div>
                        <div className="animal_selection">
                            <p>Dog</p>

                            <p>Cat</p>
                        </div>
                        
                        <div className="animal_select">
                            <div className="type_dog">
                                <PetButton animal="dog"/>
                            </div>
                            
                            <div className="type_cat">
                                <PetButton animal="cat"/>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </>
    );
}

export default Home;