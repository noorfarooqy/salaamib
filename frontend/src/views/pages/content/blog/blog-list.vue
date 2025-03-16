<template>
  <div class="row">
    <!-- Blog Post -->
    <div class="col-md-6 col-xl-4 col-sm-12 d-md-flex d-sm-block">
      <div class="blog grid-blog flex-fill">
        <div class="blog-image">
          <a href="javascript:;"
            ><img
              class="img-fluid"
              src="@/assets/img/category/blog-1.jpg"
              alt="Post Image"
          /></a>
          <div class="blog-views">
            <p>31</p>
            <span>AUG</span>
          </div>
        </div>
        <div class="blog-content">
          <ul class="entry-meta meta-item">
            <li>
              <div class="post-group d-flex align-items-center">
                <div class="post-widget">
                  <span>Advertising</span>
                </div>
                <div class="post-author">
                  <router-link to="/profile">
                    <img src="@/assets/img/profiles/avatar-12.jpg" alt="Post Author" />
                    <span>
                      <span class="post-title">Alex Campbell</span>
                    </span>
                  </router-link>
                </div>
              </div>
            </li>
          </ul>
          <h3 class="blog-title">
            <a href="javascript:;">
              Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos
              de texto.</a
            >
          </h3>
          <p>
            Lorem ipsum dolor sit amet, consectetur em adipiscing elit, sed do eiusmod
            tempor.
          </p>
          <div class="edit-options">
            <div class="edit-delete-btn">
              <a
                href="javascript:;"
                data-bs-toggle="modal"
                data-bs-target="#edit_blog"
                class="text-muted"
                ><i class="feather feather-edit me-1"></i> Edit</a
              >
              <a
                href="javascript:;"
                class="text-muted"
                data-bs-toggle="#"
                data-bs-target="#deleteModal"
                ><i class="feather feather-trash-2 ms-1"></i> Delete</a
              >
            </div>
            <div class="text-end inactive-style">
              <a
                href="javascript:void(0);"
                class="text-muted"
                data-bs-target="#deleteNotConfirmModal"
                ><i class="feather feather-alert-circle me-1"></i> Active</a
              >
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- /Blog Post -->

    <!-- Blog Post -->
    <div class="col-md-6 col-xl-4 col-sm-12 d-md-flex d-sm-block">
      <div class="blog grid-blog flex-fill">
        <div class="blog-image">
          <a href="javascript:;"
            ><img
              class="img-fluid"
              src="@/assets/img/category/blog-2.jpg"
              alt="Post Image"
          /></a>
          <div class="blog-views">
            <p>30</p>
            <span>May</span>
          </div>
        </div>
        <div class="blog-content">
          <ul class="entry-meta meta-item">
            <li>
              <div class="post-group d-flex align-items-center">
                <div class="post-widget">
                  <span>Advertising</span>
                </div>
                <div class="post-author">
                  <router-link to="/profile">
                    <img src="@/assets/img/profiles/avatar-04.jpg" alt="Post Author" />
                    <span>
                      <span class="post-title">Barbara Moore</span>
                    </span>
                  </router-link>
                </div>
              </div>
            </li>
          </ul>
          <h3 class="blog-title">
            <a href="javascript:;">
              Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos
              de texto.</a
            >
          </h3>
          <p>
            Lorem ipsum dolor sit amet, consectetur em adipiscing elit, sed do eiusmod
            tempor.
          </p>
          <div class="edit-options">
            <div class="edit-delete-btn">
              <a
                href="javascript:;"
                data-bs-toggle="modal"
                data-bs-target="#edit_blog"
                class="text-muted"
                ><i class="feather feather-edit me-1"></i> Edit</a
              >
              <a
                href="javascript:;"
                class="text-muted"
                data-bs-toggle="#"
                data-bs-target="#deleteModal"
                ><i class="feather feather-trash-2 ms-1"></i> Delete</a
              >
            </div>
            <div class="text-end inactive-style">
              <a
                href="javascript:void(0);"
                class="text-muted"
                data-bs-target="#deleteNotConfirmModal"
                ><i class="feather feather-alert-circle me-1"></i> Active</a
              >
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- /Blog Post -->

    <!-- Blog Post -->
    <div class="col-md-6 col-xl-4 col-sm-12 d-md-flex d-sm-block">
      <div class="blog grid-blog flex-fill">
        <div class="blog-image">
          <a href="javascript:;"
            ><img
              class="img-fluid"
              src="@/assets/img/category/blog-3.jpg"
              alt="Post Image"
          /></a>
          <div class="blog-views">
            <p>29</p>
            <span>Jan</span>
          </div>
        </div>
        <div class="blog-content">
          <ul class="entry-meta meta-item">
            <li>
              <div class="post-group d-flex align-items-center">
                <div class="post-widget">
                  <span>Advertising</span>
                </div>
                <div class="post-author">
                  <router-link to="/profile">
                    <img src="@/assets/img/profiles/avatar-02.jpg" alt="Post Author" />
                    <span>
                      <span class="post-title">Brian Johnson</span>
                    </span>
                  </router-link>
                </div>
              </div>
            </li>
          </ul>
          <h3 class="blog-title">
            <a href="javascript:;">
              Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos
              de texto.</a
            >
          </h3>
          <p>
            Lorem ipsum dolor sit amet, consectetur em adipiscing elit, sed do eiusmod
            tempor.
          </p>
          <div class="edit-options">
            <div class="edit-delete-btn">
              <a
                href="javascript:;"
                data-bs-toggle="modal"
                data-bs-target="#edit_blog"
                class="text-muted"
                ><i class="feather feather-edit me-1"></i> Edit</a
              >
              <a
                href="javascript:;"
                class="text-muted ms-3"
                data-bs-toggle="#"
                data-bs-target="#deleteModal"
                ><i class="feather feather-trash-2 ms -1"></i> Delete</a
              >
            </div>
            <div class="text-end inactive-style">
              <a
                href="javascript:void(0);"
                class="text-muted"
                data-bs-target="#deleteNotConfirmModal"
                ><i class="feather feather-alert-circle me-1"></i> Active</a
              >
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- /Blog Post -->

    <!-- Blog Post -->
    <div class="col-md-6 col-xl-4 col-sm-12 d-md-flex d-sm-block">
      <div class="blog grid-blog flex-fill">
        <div class="blog-image">
          <a href="javascript:;"
            ><img
              class="img-fluid"
              src="@/assets/img/category/blog-4.jpg"
              alt="Post Image"
          /></a>
          <div class="blog-views">
            <p>10</p>
            <span>AUG</span>
          </div>
        </div>
        <div class="blog-content">
          <ul class="entry-meta meta-item">
            <li>
              <div class="post-group d-flex align-items-center">
                <div class="post-widget">
                  <span>Advertising</span>
                </div>
                <div class="post-author">
                  <router-link to="/profile">
                    <img src="@/assets/img/profiles/avatar-05.jpg" alt="Post Author" />
                    <span>
                      <span class="post-title">Greg Lynch</span>
                    </span>
                  </router-link>
                </div>
              </div>
            </li>
          </ul>
          <h3 class="blog-title">
            <a href="javascript:;">
              Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos
              de texto.</a
            >
          </h3>
          <p>
            Lorem ipsum dolor sit amet, consectetur em adipiscing elit, sed do eiusmod
            tempor.
          </p>
          <div class="edit-options">
            <div class="edit-delete-btn">
              <a
                href="javascript:;"
                data-bs-toggle="modal"
                data-bs-target="#edit_blog"
                class="text-muted"
                ><i class="feather feather-edit me-1"></i> Edit</a
              >
              <a
                href="javascript:;"
                class="text-muted"
                data-bs-toggle="#"
                data-bs-target="#deleteModal"
                ><i class="feather feather-trash-2 ms-1"></i> Delete</a
              >
            </div>
            <div class="text-end inactive-style">
              <a
                href="javascript:void(0);"
                class="text-muted"
                data-bs-target="#deleteNotConfirmModal"
                ><i class="feather feather-alert-circle me-1"></i> Active</a
              >
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- /Blog Post -->

    <!-- Blog Post -->
    <div class="col-md-6 col-xl-4 col-sm-12 d-md-flex d-sm-block">
      <div class="blog grid-blog flex-fill">
        <div class="blog-image">
          <a href="javascript:;"
            ><img
              class="img-fluid"
              src="@/assets/img/category/blog-5.jpg"
              alt="Post Image"
          /></a>
          <div class="blog-views">
            <p>11</p>
            <span>FEB</span>
          </div>
        </div>
        <div class="blog-content">
          <ul class="entry-meta meta-item">
            <li>
              <div class="post-group d-flex align-items-center">
                <div class="post-widget">
                  <span>Advertising</span>
                </div>
                <div class="post-author">
                  <router-link to="/profile">
                    <img src="@/assets/img/profiles/avatar-11.jpg" alt="Post Author" />
                    <span>
                      <span class="post-title">Jennifer Floyd</span>
                    </span>
                  </router-link>
                </div>
              </div>
            </li>
          </ul>
          <h3 class="blog-title">
            <a href="javascript:;">
              Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos
              de texto.</a
            >
          </h3>
          <p>
            Lorem ipsum dolor sit amet, consectetur em adipiscing elit, sed do eiusmod
            tempor.
          </p>
          <div class="edit-options">
            <div class="edit-delete-btn">
              <a
                href="javascript:;"
                data-bs-toggle="modal"
                data-bs-target="#edit_blog"
                class="text-muted"
                ><i class="feather feather-edit me-1"></i> Edit</a
              >
              <a
                href="javascript:;"
                class="text-muted"
                data-bs-toggle="#"
                data-bs-target="#deleteModal"
                ><i class="feather feather-trash-2 ms-1"></i> Delete</a
              >
            </div>
            <div class="text-end inactive-style">
              <a
                href="javascript:void(0);"
                class="text-muted"
                data-bs-target="#deleteNotConfirmModal"
                ><i class="feather feather-alert-circle me-1"></i> Active</a
              >
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- /Blog Post -->

    <!-- Blog Post -->
    <div class="col-md-6 col-xl-4 col-sm-12 d-md-flex d-sm-block">
      <div class="blog grid-blog flex-fill">
        <div class="blog-image">
          <a href="javascript:;"
            ><img
              class="img-fluid"
              src="@/assets/img/category/blog-6.jpg"
              alt="Post Image"
          /></a>
          <div class="blog-views">
            <p>12</p>
            <span>JUN</span>
          </div>
        </div>
        <div class="blog-content">
          <ul class="entry-meta meta-item">
            <li>
              <div class="post-group d-flex align-items-center">
                <div class="post-widget">
                  <span>Advertising</span>
                </div>
                <div class="post-author">
                  <router-link to="/profile">
                    <img src="@/assets/img/profiles/avatar-06.jpg" alt="Post Author" />
                    <span>
                      <span class="post-title">Karlene Chaidez </span>
                    </span>
                  </router-link>
                </div>
              </div>
            </li>
          </ul>
          <h3 class="blog-title">
            <a href="javascript:;">
              Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos
              de texto.</a
            >
          </h3>
          <p>
            Lorem ipsum dolor sit amet, consectetur em adipiscing elit, sed do eiusmod
            tempor.
          </p>
          <div class="edit-options">
            <div class="edit-delete-btn">
              <a
                href="javascript:;"
                data-bs-toggle="modal"
                data-bs-target="#edit_blog"
                class="text-muted"
                ><i class="feather feather-edit me-1"></i> Edit</a
              >
              <a
                href="javascript:;"
                class="text-muted"
                data-bs-toggle="#"
                data-bs-target="#deleteModal"
                ><i class="feather feather-trash-2 ms-1"></i> Delete</a
              >
            </div>
            <div class="text-end inactive-style">
              <a
                href="javascript:void(0);"
                class="text-muted"
                data-bs-target="#deleteNotConfirmModal"
                ><i class="feather feather-alert-circle me-1"></i> Active</a
              >
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- /Blog Post -->
  </div>
  <!-- Pagination -->
  <div class="row">
    <div class="col-md-12">
      <div class="pagination-tab d-flex justify-content-center">
        <ul class="pagination mb-0">
          <li class="page-item disabled">
            <a class="page-link" href="javascript:;" tabindex="-1"
              ><i class="feather-chevron-left mr-2"></i>Previous</a
            >
          </li>
          <li class="page-item"><a class="page-link" href="javascript:;">1</a></li>
          <li class="page-item active">
            <a class="page-link" href="javascript:;"
              >2 <span class="sr-only">(current)</span></a
            >
          </li>
          <li class="page-item"><a class="page-link" href="javascript:;">3</a></li>
          <li class="page-item"><a class="page-link" href="javascript:;">4</a></li>
          <li class="page-item">
            <a class="page-link" href="javascript:;"
              >Next<i class="feather-chevron-right ml-2"></i
            ></a>
          </li>
        </ul>
      </div>
    </div>
  </div>
  <!-- /Pagination -->
</template>
