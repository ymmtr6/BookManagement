import React from "react";
import { ContentCard } from "./ContentCard";
//import { Link } from "react-router-dom";

const Books = ({ books }) => {
  return (
    books.map((book, index) => (
      <ContentCard
        pageName={book.title}
        imgSrc={"thumbnail" in book ? (book.thumbnail) : "./img/noimage.png"}
        discription={book.authors instanceof Array ? book.authors.join(" ") : book.authors}
        key={book.isbn}
      />
    ))

  )
};

export default Books
    /*
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
*/
