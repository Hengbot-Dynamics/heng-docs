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
    title: 'Introducing Sparky: A Highly Advanced and Lifelike Robotic Dog',
    Gif: 'img/sparky.gif',
    description: (
      <>Sparky is the World’s first lifelike robotic dog.<br/>It can move agilely like a real dog. 
      Its advanced motion editing modes allow it to perform agile and elegant movements.</>
    ),
  },
];

function Feature({title, Gif, description}: FeatureItem) {
  return (
    <div className={clsx('col col--12')}>
      <div className="text--center">
        <Heading as="h3" style={{ color: 'white' }}>{title}</Heading>
        <img src={Gif} alt={title} className={styles.featureGif} role="img" style={{ borderRadius: '10px' }}/>
      </div>
      <div className="text--center padding-horiz--md" style={{ color: 'white' }}>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures(): JSX.Element {
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
