import React, {useState, useEffect} from 'react';
import axios from 'axios';
import Form from './Form';

const App = () => {

  const [posts, setPosts] = useState([])

  useEffect(() => {
    axios.get('https://jsonplaceholder.typicode.com/posts')
    .then(res => {
        setPosts(res.data)
    })
  }, [])

    return (
      <div>
        <div>
            <ul>
            { posts.map( post => {
              <li> 
                { post.title }
              </li>
            })}
            </ul>
            
        </div>
        <Form />
      </div>
    );
}

export default App;
