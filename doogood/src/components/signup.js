import React,{ useState } from 'react';
import cs from './styles/signup.module.css';

function Signup(props) {
    const [x, setX] = useState(0);
    const [formData, setFormData] = useState({});
  
    function ngoClicked() {
      setX(1);
    }
  
    function philClicked() {
      setX(2);
    }
  
    function handleFormSubmit(event) {
      event.preventDefault();
      // Assuming you have unique IDs for your form fields.
      const formElements = event.target.elements;
      const formValues = {};
      
      for (let i = 0; i < formElements.length; i++) {
        const element = formElements[i];
        if (element.tagName === 'INPUT' || element.tagName === 'SELECT') {
          formValues[element.name] = element.value;
        }
      }
  
      // Save the form data as JSON
      const jsonData = JSON.stringify(formValues);
  
      // You can now write jsonData to a file or send it to a server.
      console.log('Form data in JSON:', jsonData);
    }
  
    if (x === 0) {
      return (
        <div>
          <h2>
            To create a centralized platform that makes it easy for philanthropists to discover and support NGOs working in areas they are passionate about.
            Create your first profile as an ..
          </h2>
          <button className={cs.signupbts} onClick={philClicked}>
            Philanthropist
          </button>
          <button className={cs.signupbts} onClick={ngoClicked}>
            NGO
          </button>
        </div>
      )
    } else if (x === 1) {
      return (
        <div>
          <h2>Create Profile</h2>
          <form action="" id="doogoodngo" onSubmit={handleFormSubmit}>
            <label htmlFor="name">Name of the Organisation</label><br />
            <input type="text" id="name" size="40" name="name" /><br />
            <label htmlFor="loc">Location</label><br />
            <input type="text" id="loc" size="40" name="loc" /><br />
            <label htmlFor="goal">End Goal</label><br />
            <select id="goal" name="goal">
                <option value="Literacy">Literacy</option>
                <option value="Health">Health</option>
                <option value="Sanity">Sanity</option>
                <option value="Zero Pollution">Zero Pollution</option>
                <option value="Employment">Employment</option>
                <option value="Women & Child Safety">Women & Child Safety</option>
                <option value="Zero Poverty">Zero Poverty</option>
                <option value="Infrastructure">Infrastructure</option>
                <option value="Life Support">Life Support</option>
            </select><br />
            <label htmlFor="fund">Fund Needed</label><br />
            <input type="text" id="fund" size="40" name="fund" /><br />
            <button type="submit">Submit</button>
          </form>
        </div>
      )
    } else if (x === 2) {
      return (
        <div>
          <h2>Create Profile</h2>
          <form action="" id="doogoodngo" onSubmit={handleFormSubmit}>
            <label htmlFor="pname">Name</label><br />
            <input type="text" id="pname" size="40" name="pname" /><br />
            <label htmlFor="mail">Email</label><br />
            <input type="text" id="mail" size="40" name="mail" /><br />
            <label htmlFor="priority">Preference</label><br />
            <select id="priority" name="priority">
                <option value="Literacy">Literacy</option>
                <option value="Health">Health</option>
                <option value="Sanity">Sanity</option>
                <option value="Zero Pollution">Zero Pollution</option>
                <option value="Employment">Employment</option>
                <option value="Women & Child Safety">Women & Child Safety</option>
                <option value="Zero Poverty">Zero Poverty</option>
                <option value="Infrastructure">Infrastructure</option>
                <option value="Life Support">Life Support</option>
            </select><br />
            <label htmlFor="fund">Fund Provided</label><br />
            <input type="text" id="fund" size="40" name="fund" /><br />
            <button type="submit">Submit</button>
          </form>
        </div>
      )
    } else {
      // Handle other cases if needed
      return null;
    }
  }
  
  export default Signup;





