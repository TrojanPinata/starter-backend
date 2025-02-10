import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";

const base_url = "http://localhost:5000";

const sub = "folder2";

function Home() {
   const [images, setImages] = useState([]);

   useEffect(() => {
      fetch(`${base_url}/api/image_list/${sub}`)
         .then(response => response.json())
         .then(imageList => {
              setImages(imageList.map(img => ({
                  src: `/api/get_image/${sub}/${img}`,
                  name: img
            })));
         })
         .catch(error => console.error("Error fetching images:", error));
   }, []);

   return (
      <div>
         <h1>Image Gallery</h1>
         <div style={{ display: "flex", flexWrap: "wrap" }}>
            {images.map((image, index) => (
               <div key={index} style={{ margin: "10px" }}>
                  <img src={image.src} alt={image.name} style={{ width: "200px", height: "auto" }} />
                  <p>{image.name}</p>
               </div>
            ))}
         </div>
         <Link to="/">go home</Link>
      </div>
   );
}

export default Home;
