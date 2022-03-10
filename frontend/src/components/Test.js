import React, {useState, useEffect} from 'react'
import axios from 'axios'

const Test = () => {

    const [post, setPosts] = useState([])

    useEffect(() => {
        axios.get('http://127.0.0.1:5000/chat')
        .then(res => {
            setPosts(res.data)
            console.log(res.data)
        })
    }, [])

    return (
        <div>
            <p> {post.success} </p>
        </div>
    )
}

export default Test