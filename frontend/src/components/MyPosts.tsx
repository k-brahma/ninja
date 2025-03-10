import React, { useEffect, useState } from 'react';

function MyPosts() {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    // APIから自分の投稿を取得する処理をここに追加
  }, []);

  return (
    <div>
      <h1>My Posts</h1>
      <ul>
        {posts.map((post: any) => (
          <li key={post.id}>{post.title}</li>
        ))}
      </ul>
    </div>
  );
}

export default MyPosts; 