import "../styles/About.css"

function About(){
    return(    
        <div>

            <body>
                <div className="about-page">
                    <div className="mission">
                        <div className="mission-text">
                            <h1>About Us</h1>
                            <p>
                                This website was created as apart of a group project with the goal of helping pets find their forever home.
                                Our mission is to ensure these pets are placed in safe and nurturing environments. 
                                Currently, we are focused on serving the Connecticut and New York areas.
                                We aim to make the website accesible to everyone, with a user-friendly design that minimizes scrolling and makes it eay to find what you need.
                            </p>
                        </div>
                        <div className="mission-image">
                            <img src="../aboutPets.png"/>
                        </div>
                    </div>
                </div>

                <div className="team">
                    <h2>Meet our Team</h2>
                    <div className="team-members">
                        <div className="team-member" >
                            <img src="../cat16.png" alt="ShaniquePic"/>
                            <h3>Shanique</h3>
                        </div>
                        <div className="team-member">
                        <img src="../dog4.png" alt="NicholePic"/>
                            <h3>Nichole</h3>
                        </div>
                        <div className="team-member">
                            <img src="../dog3.png" alt="EthanPic"/>
                            <h3>Ethan</h3>
                        </div>
                        <div className="team-member">
                            <img src="../cat12.png" alt="AlenPic"/>
                            <h3>Allen</h3>
                        </div>
                    </div>
                </div>
            </body>

        </div>
    );
}

export default About;