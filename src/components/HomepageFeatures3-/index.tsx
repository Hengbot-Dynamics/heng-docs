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
    title: 'High-speed dynamic motion',
    Gif: 'img/speed.gif',
    description: (
    <>with a maximum forward speed of 0.5m/s and a maximum backward speed of 0.4m/s.</>
    ),
  },
];

function Feature({ title, Gif, description }) {
  return (
    <div className="col col--12">
      {/* 使用Flexbox布局，图片在左侧，文本内容在右侧 */}
      <div className="feature-content" style={{ display: 'flex', alignItems: 'flex-start' }}>
        {/* 图片在左侧 */}
        <img 
          src={Gif} 
          alt={title} 
          className={styles.featureGif} 
          style={{ borderRadius: '10px', marginRight: '20px', objectFit: 'cover'}} 
        />
        {/* 描述和标题容器 */}
        <div className="text-container" style={{ flexGrow: 1, textAlign: 'right' }}>
          <Heading as="h1" style={{ color: 'white', marginTop: '20px', marginBottom: '60px' }}>{title}</Heading>
          <Heading as="p" style={{color: 'white', }}>
          {description}</Heading>
        </div>
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
