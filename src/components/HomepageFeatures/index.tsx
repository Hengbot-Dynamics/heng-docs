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
    title: '初识哮天',
    subtitle: '集交互性和可扩展性于一身的高动态机器狗',
    description: (
      <>哮天是一款灵活敏捷的机器人伴侣，配备 Cortex-A7 1GHz 处理器。通过优先考虑美学和用户体验，
      多年来我们完善了SPARKY的设计和结构。它的支腿采用模块化连杆，并集成了 AIA 执行器单元，让您可以像更换四轮驱动汽车电机一样轻松升级 SPARKY 的动力系统，并像更换手机壳一样定制独一无二的 SPARKY。</>
    ),
    Gif: 'img/sparky.gif',
  },
];

function Feature({title, subtitle, description, Gif}: FeatureItem) {
  return (
    <div className={clsx('col col--12')}>
    <div className="text--center">
      <Heading as="h1" style={{ color: 'white',marginBottom: '20px' }}>{title}</Heading>
      <Heading as="h2" style={{ color: 'white',marginBottom: '30px' }}>{subtitle}</Heading>
      <div className="text--center padding-horiz--md" style={{ color: 'white' }}>
    </div>
      <img src={Gif} alt={title} className={styles.featureGif} role="img" style={{ borderRadius: '10px', marginBottom: '20px'}}/>
    </div>
    <Heading as="p" style={{color: 'white', marginTOP: '30px'}}>
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
