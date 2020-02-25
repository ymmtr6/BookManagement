import React from "react";

export function ContentCard(props) {
  return (
    <div className="ContentCard p-4 hvr-grow">
      <div className="max-w-sm rounded overflow-hidden shadow-lg text-center">
        <img
          className="h-128 w-64 mx-auto"
          src={props.imgSrc}
          alt="book thumnail"
        ></img>
        <div className="px-6 py-4">
          <div className="font-bold text-xl mb-2 w-64">{props.pageName}</div>
          <p className="text-gray-700 text-base w-64">
            {props.discription}
          </p>
        </div>
      </div>
    </div>
  );
}
