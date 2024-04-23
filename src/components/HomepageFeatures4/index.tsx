import clsx from 'clsx';
import Heading from '@theme/Heading';
import styles from './styles.module.css';

type FeatureItem = {
  title: string;
  Gif: string;
  description: JSX.Element;
};

const FeatureList: FeatureItem[] = [
  {
    title: 'Around the Y-axis -75°~120° ',
    Gif: 'img/y_axis.gif',
    description: (
      <></>
    ),
  },
  {
    title: 'Around the X-axis -50°~110°',
    Gif: 'img/x_axis.gif',
    description: (
      <></>
    ),
  },
  {
    title: 'Along the Z-axis 70mm~170mm',
    Gif: 'img/z_axis.gif',
    description: (
      <></>
    ),
  },
];


function Feature({title, Gif, description}: FeatureItem) {
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center">
      <Heading as="h3" style={{ color: 'white', marginTop: '0px', marginBottom: '20px' }}>{title}</Heading>
        <img src={Gif} alt={title} className={styles.featureGif}  role="img" style={{ borderRadius: '10px', marginBottom: '0px'}}/>
      </div>
      <div className="text--center padding-horiz--md">
        <p>{description}</p>
      </div>
    </div>
  );
}

function Feature1({title, Gif, description}: FeatureItem) {
  return (
    <div className={clsx('col col--12')}>
      <div className="text--center">
        <img src={Gif} alt={title} className={styles.featureGif} role="img" />
      </div>
      <div className="text--center padding-horiz--md">
        <Heading as="h3">{title}</Heading>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures1(): JSX.Element {
  return (
    <section className={styles.features}>
      <div className={clsx('hero hero')} style={{ backgroundColor: 'rgb(28 28 28)' }}>
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
