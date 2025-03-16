<template>
  <div class="row">
    <div class="col-md-6">
      <div class="card bg-white">
        <div class="card-header">
          <h5 class="card-title">Bottom line tabs</h5>
        </div>
        <div class="card-body">
          <ul class="nav nav-tabs nav-tabs-bottom">
            <li class="nav-item">
              <a class="nav-link active" href="#bottom-tab1" data-bs-toggle="tab">Home</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#bottom-tab2" data-bs-toggle="tab">Profile</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#bottom-tab3" data-bs-toggle="tab">Messages</a>
            </li>
          </ul>

          <div class="tab-content">
            <div class="tab-pane show active" id="bottom-tab1">Tab content 1</div>
            <div class="tab-pane" id="bottom-tab2">Tab content 2</div>
            <div class="tab-pane" id="bottom-tab3">Tab content 3</div>
          </div>
        </div>
      </div>
    </div>
    <div class="col-md-6">
      <div class="card bg-white">
        <div class="card-header">
          <h5 class="card-title">Bottom line justified</h5>
        </div>
        <div class="card-body">
          <ul class="nav nav-tabs nav-tabs-bottom nav-justified">
            <li class="nav-item">
              <a
                class="nav-link active"
                href="#bottom-justified-tab1"
                data-bs-toggle="tab"
                >Home</a
              >
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#bottom-justified-tab2" data-bs-toggle="tab"
                >Profile</a
              >
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#bottom-justified-tab3" data-bs-toggle="tab"
                >Messages</a
              >
            </li>
          </ul>
          <div class="tab-content">
            <div class="tab-pane show active" id="bottom-justified-tab1">
              Tab content 1
            </div>
            <div class="tab-pane" id="bottom-justified-tab2">Tab content 2</div>
            <div class="tab-pane" id="bottom-justified-tab3">Tab content 3</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
