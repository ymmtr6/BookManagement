import React from "react";
import { ContentCard } from "./ContentCard";
//import { Link } from "react-router-dom";

const Books = ({ books }) => {
  return (
    <div className="inline-block">{
      books.map((book) => (
        <ContentCard
          pageName={book.title}
          imgSrc={"thumbnail" in book ? (book.thumbnail) : "./img/noimage.png"}
          discription={book.authors instanceof Array ? book.authors.join(" ") : book.authors}
        />
      ))
    }
    </div>
  )
};

export default Books
    /*
<ContentCard
pageName="SNS"
imgSrc="https://source.unsplash.com/random/1600x900/"
discription="SNSSample page!"
/>
*/
