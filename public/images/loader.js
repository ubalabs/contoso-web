// See:
// https://nextjs.org/docs/app/api-reference/next-config-js/images

export default function myImageLoader({ src, width, quality }) {
    let url=`${src}?w=${width}&q=${quality || 75}`;
    //console.log('myImageLoader returns:', url);
    return url;
}