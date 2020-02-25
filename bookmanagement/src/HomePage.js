import React from "react";
import { ContentCard } from "./ContentCard";
import { Link } from "react-router-dom";
import { Header } from "./Header";

export function HomePage() {
  return (
    <div className="HomePage">
      <Header />
      <div className="flex mb-4">
        <Link to="#" className="w-1/3">
          <ContentCard
            pageName="SNS"
            imgSrc="https://source.unsplash.com/random/1600x900/"
            discription="SNSSample page!"
          />
        </Link>
      </div>
    </div>
  );
}
