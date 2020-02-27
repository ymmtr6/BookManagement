import React from "react";
import { ContentCard } from "./ContentCard";
//import { Link } from "react-router-dom";

class Books extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      books: this.props.books
    };
  }

  render() {
    return (
      this.props.books.map((book, index) => (
        <ContentCard
          pageName={book.title}
          imgSrc={"thumbnail" in book ? (book.thumbnail) : "./img/noimage.png"}
          discription={book.authors instanceof Array ? book.authors.join(" ") : book.authors}
          key={book.isbn}
        />
      ))
    )
  }
}

export default Books
