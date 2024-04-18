import React from 'react';
import Slider from 'react-slick';

const settings = {
  dots: true,
  infinite: true,
  speed: 500,
  slidesToShow: 1,
  slidesToScroll: 1,
  autoplay: true,
};

const images = [
  'img/slide1.jpg',
  'img/slide2.jpg',
  'img/slide3.jpg',
  // 更多图片路径
];

const ImageSlider = () => (
  <Slider {...settings}>
    {images.map((image, index) => (
      <div key={index}>
        <img src={image} alt={`Slide ${index + 1}`} />         </div>       ))}     </Slider>   );   
        export default ImageSlider;