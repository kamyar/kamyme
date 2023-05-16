import React from 'react';

import './App.css';

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import {
  faGithub,
  faLinkedin,
  faMedium,
  faStackOverflow
} from '@fortawesome/free-brands-svg-icons';


function App() {
  return (
    <main>
      <highlight>
        <h1>Kamyar Ghasemlou</h1>
        <h2>
          Hi there, welcome to my homepage!
        </h2>
        <p>
          I am a Software Engineer currently working @ <a href="https://wolt.com/">Wolt</a> in Berlin.
        </p>
        <p>
          I am passionate about building products that help people. You can access my <a href="Kamyar_Ghasemlou_CV.pdf">CV</a> here.
        </p>
        <p>
          Below you can find some of my social links. {/*or contact me via <email> my_name@current_website</email>.*/}
        </p>
        <logos>
          <a href="https://github.com/kamyar">
            <FontAwesomeIcon icon={faGithub} />
          </a>
          <a href="https://www.linkedin.com/in/ghasemlou/">
            <FontAwesomeIcon icon={faLinkedin} />
          </a>
          <a href="https://medium.com/@kamyarg">
            <FontAwesomeIcon icon={faMedium} />
          </a>
          <a href="https://stackoverflow.com/users/1329429/">
            <FontAwesomeIcon icon={faStackOverflow} />
          </a>
        </logos>
       </highlight>
    </main>
  );
}

export default App;
