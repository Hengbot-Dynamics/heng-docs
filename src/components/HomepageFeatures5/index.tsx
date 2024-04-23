import clsx from 'clsx';
import Heading from '@theme/Heading';
import styles from './styles.module.css';

interface FeatureItem {
  title: string;
  subtitle: string;
  Gif: string;
  description: JSX.Element;
};


const FeatureList: FeatureItem[] = [
  {
    title: 'Integrated Head Design',
    subtitle: 'Highly integrated universal head module,the central hub for robot is general decision-making.',
    description: (
      <>Integrating sensors and computing in SPARKY's head, mimicking the cortical structure of the brain.<br/>All actuators connected to the head like a neural center,<br/
      >endowing SPARKY with sensing, decision-making, and interactive capabilities.</>
    ),
    Gif: 'img/header_identification.jpg',
  },
];

function Feature({title, subtitle, description, Gif}: FeatureItem) {
  return (
    <div className={clsx('col col--12')}>
      <div className="text--center">
        <Heading as="h1" style={{ color: 'white',marginBottom: '40px' }}>{title}</Heading>
        <Heading as="h3" style={{ color: 'white', marginBottom: '30px' }}>{subtitle}</Heading>
        <div className="text--center padding-horiz--md" style={{ color: 'white',marginBottom: '40px'}}>
      </div>
        <img src={Gif} alt={title} className={styles.featureGif} role="img" style={{ borderRadius: '10px', marginBottom: '20px' }}/>
      </div>
      <Heading as="p" style={{color: 'white', }}>
          {description}</Heading>
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


