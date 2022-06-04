import React from "react";

export default function Rating({ value, text }) {
  return (
    <>
      <div>
        <span className="tw-text-yellow-500 tw-mr-1">
          <i
            className={
              value >= 1
                ? "fas fa-star"
                : value >= 0.5
                ? "fas fa-star-half-alt"
                : "fas fa-star"
            }
          ></i>
        </span>
        <span className="tw-text-yellow-500 tw-mr-1">
          <i
            className={
              value >= 2
                ? "fas fa-star"
                : value >= 1.5
                ? "fas fa-star-half-alt"
                : "fas fa-star"
            }
          ></i>
        </span>
        <span className="tw-text-yellow-500 tw-mr-1">
          <i
            className={
              value >= 4
                ? "fas fa-star"
                : value >= 3.5
                ? "fas fa-star-half-alt"
                : "fas fa-star"
            }
          ></i>
        </span>
        <br />
        <span className="tw-text-slate-400 tw-text-sm ">{text}</span>
      </div>
    </>
  );
}
