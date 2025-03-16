<template>
  <div class="row">
    <div class="col-md-6">
      <div class="card bg-white">
        <div class="card-header">
          <h5 class="card-title">Top line tabs</h5>
        </div>
        <div class="card-body">
          <ul class="nav nav-tabs nav-tabs-top">
            <li class="nav-item">
              <a class="nav-link active" href="#top-tab1" data-bs-toggle="tab">Home</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#top-tab2" data-bs-toggle="tab">Profile</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#top-tab3" data-bs-toggle="tab">Messages</a>
            </li>
          </ul>
          <div class="tab-content">
            <div class="tab-pane show active" id="top-tab1">Tab content 1</div>
            <div class="tab-pane" id="top-tab2">Tab content 2</div>
            <div class="tab-pane" id="top-tab3">Tab content 3</div>
          </div>
        </div>
      </div>
    </div>

    <div class="col-md-6">
      <div class="card bg-white">
        <div class="card-header">
          <h5 class="card-title">Top line justified</h5>
        </div>
        <div class="card-body">
          <ul class="nav nav-tabs nav-tabs-top nav-justified">
            <li class="nav-item">
              <a class="nav-link active" href="#top-justified-tab1" data-bs-toggle="tab"
                >Home</a
              >
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#top-justified-tab2" data-bs-toggle="tab"
                >Profile</a
              >
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#top-justified-tab3" data-bs-toggle="tab"
                >Messages</a
              >
            </li>
          </ul>
          <div class="tab-content">
            <div class="tab-pane show active" id="top-justified-tab1">Tab content 1</div>
            <div class="tab-pane" id="top-justified-tab2">Tab content 2</div>

            <div class="tab-pane" id="top-justified-tab3">Tab content 3</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
